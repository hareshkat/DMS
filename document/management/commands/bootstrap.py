from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from river.models import State, Workflow, TransitionApprovalMeta, TransitionMeta

from document.models import Document
from employee.models import DmsUser


# noinspection DuplicatedCode
class Command(BaseCommand):
    help = 'Bootstrapping database with necessary items'

    @transaction.atomic()
    def handle(self, *args, **options):
        workflow_content_type = ContentType.objects.get_for_model(Workflow)
        content_type = ContentType.objects.get_for_model(Document)

        add_document_permission = Permission.objects.get(codename="add_document", content_type=content_type)
        change_document_permission = Permission.objects.get(codename="change_document", content_type=content_type)
        delete_document_permission = Permission.objects.get(codename="delete_document", content_type=content_type)

        view_workflow_permission = Permission.objects.get(codename="view_workflow", content_type=workflow_content_type)

        creator_group, _ = Group.objects.update_or_create(name="creator")
        creator_group.permissions.set([add_document_permission, change_document_permission, view_workflow_permission])
        reviewer_group, _ = Group.objects.update_or_create(name="reviewer")
        reviewer_group.permissions.set([change_document_permission, delete_document_permission, view_workflow_permission])
        approver_group, _ = Group.objects.update_or_create(name="approver")
        approver_group.permissions.set([change_document_permission, view_workflow_permission])

        open_state, _ = State.objects.update_or_create(label="Open", slug="open")
        in_progress_state, _ = State.objects.update_or_create(label="In Progress", slug="in_progress")
        processing_state, _ = State.objects.update_or_create(label="Processing", slug="processing")
        reviewed_state, _ = State.objects.update_or_create(label="Reviewed", slug="reviewed")
        re_open_state, _ = State.objects.update_or_create(label="Re Open", slug="re_open")
        approved_state, _ = State.objects.update_or_create(label="Approved", slug="approved")

        workflow, _ = Workflow.objects.update_or_create(content_type=content_type, field_name="status", defaults={"initial_state": open_state})

        open_to_in_progress, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=open_state, destination_state=in_progress_state)
        in_progress_to_processing, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=in_progress_state, destination_state=processing_state)
        processing_to_reviewed, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=processing_state, destination_state=reviewed_state)
        processing_to_re_open, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=processing_state, destination_state=re_open_state)
        re_open_to_in_progress, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=re_open_state, destination_state=in_progress_state)
        reviewed_to_approved, _ = TransitionMeta.objects.update_or_create(workflow=workflow, source_state=reviewed_state, destination_state=approved_state)

        open_to_in_progress_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=open_to_in_progress)
        open_to_in_progress_meta.groups.set([creator_group])

        in_progress_to_processing_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=in_progress_to_processing)
        in_progress_to_processing_meta.groups.set([reviewer_group])

        processing_to_reviewed_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=processing_to_reviewed)
        processing_to_reviewed_meta.groups.set([reviewer_group])

        processing_to_re_open_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=processing_to_re_open)
        processing_to_re_open_meta.groups.set([reviewer_group])

        re_open_to_in_progress_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=re_open_to_in_progress)
        re_open_to_in_progress_meta.groups.set([creator_group])

        reviewed_to_approved_meta, _ = TransitionApprovalMeta.objects.update_or_create(workflow=workflow, transition_meta=reviewed_to_approved)
        reviewed_to_approved_meta.groups.set([approver_group])

        root = DmsUser.objects.filter(username="admin").first() or DmsUser.objects.create_superuser("admin", "", "admin")
        root.groups.set([creator_group, reviewer_group, approver_group])

        haresh = DmsUser.objects.filter(username="user1").first() or DmsUser.objects.create_user("haresh", password="user1", is_staff=True)
        haresh.groups.set([reviewer_group])

        mahesh = DmsUser.objects.filter(username="user2").first() or DmsUser.objects.create_user("mahesh", password="user2", is_staff=True)
        mahesh.groups.set([approver_group])

        self.stdout.write(self.style.SUCCESS('Successfully bootstrapped the db '))
