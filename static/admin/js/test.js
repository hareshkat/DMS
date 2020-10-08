

(function(globals) {

  var django = globals.django || (globals.django = {});


  django.pluralidx = function(count) { return (count == 1) ? 0 : 1; };


  /* gettext library */

  django.catalog = django.catalog || {};

  var newcatalog = {
    "\"{input}\" is not a valid boolean.": "\"{input}\" is not a valid boolean.",
    "\"{input}\" is not a valid choice.": "\"{input}\" is not a valid choice.",
    "\"{input}\" is not a valid path choice.": "\"{input}\" is not a valid path choice.",
    "\"{value}\" is not a valid UUID.": "\"{value}\" is not a valid UUID.",
    "A server error occurred.": "A server error occurred.",
    "A valid integer is required.": "A valid integer is required.",
    "A valid number is required.": "A valid number is required.",
    "Auth Token": "Auth Token",
    "Authentication credentials were not provided.": "Authentication credentials were not provided.",
    "Could not satisfy the request Accept header.": "Could not satisfy the request Accept header.",
    "Created": "Created",
    "Date has wrong format. Use one of these formats instead: {format}.": "Date has wrong format. Use one of these formats instead: {format}.",
    "Datetime has wrong format. Use one of these formats instead: {format}.": "Datetime has wrong format. Use one of these formats instead: {format}.",
    "Duration has wrong format. Use one of these formats instead: {format}.": "Duration has wrong format. Use one of these formats instead: {format}.",
    "Ensure that there are no more than {max_decimal_places} decimal places.": "Ensure that there are no more than {max_decimal_places} decimal places.",
    "Ensure that there are no more than {max_digits} digits in total.": "Ensure that there are no more than {max_digits} digits in total.",
    "Ensure that there are no more than {max_whole_digits} digits before the decimal point.": "Ensure that there are no more than {max_whole_digits} digits before the decimal point.",
    "Ensure this field has at least {min_length} characters.": "Ensure this field has at least {min_length} characters.",
    "Ensure this field has no more than {max_length} characters.": "Ensure this field has no more than {max_length} characters.",
    "Ensure this filename has at most {max_length} characters (it has {length}).": "Ensure this filename has at most {max_length} characters (it has {length}).",
    "Ensure this value is greater than or equal to {min_value}.": "Ensure this value is greater than or equal to {min_value}.",
    "Ensure this value is less than or equal to {max_value}.": "Ensure this value is less than or equal to {max_value}.",
    "Enter a valid \"slug\" consisting of letters, numbers, underscores or hyphens.": "Enter a valid \"slug\" consisting of letters, numbers, underscores or hyphens.",
    "Enter a valid IPv4 or IPv6 address.": "Enter a valid IPv4 or IPv6 address.",
    "Enter a valid URL.": "Enter a valid URL.",
    "Enter a valid email address.": "Enter a valid email address.",
    "Expected a date but got a datetime.": "Expected a date but got a datetime.",
    "Expected a datetime but got a date.": "Expected a datetime but got a date.",
    "Expected a dictionary of items but got type \"{input_type}\".": "Expected a dictionary of items but got type \"{input_type}\".",
    "Expected a list of items but got type \"{input_type}\".": "Expected a list of items but got type \"{input_type}\".",
    "Field filters": "Field filters",
    "Filters": "Filters",
    "Incorrect authentication credentials.": "Incorrect authentication credentials.",
    "Incorrect type. Expected URL string, received {data_type}.": "Incorrect type. Expected URL string, received {data_type}.",
    "Incorrect type. Expected pk value, received {data_type}.": "Incorrect type. Expected pk value, received {data_type}.",
    "Invalid basic header. Credentials not correctly base64 encoded.": "Invalid basic header. Credentials not correctly base64 encoded.",
    "Invalid basic header. Credentials string should not contain spaces.": "Invalid basic header. Credentials string should not contain spaces.",
    "Invalid basic header. No credentials provided.": "Invalid basic header. No credentials provided.",
    "Invalid cursor": "Invalid cursor",
    "Invalid data. Expected a dictionary, but got {datatype}.": "Invalid data. Expected a dictionary, but got {datatype}.",
    "Invalid hyperlink - Incorrect URL match.": "Invalid hyperlink - Incorrect URL match.",
    "Invalid hyperlink - No URL match.": "Invalid hyperlink - No URL match.",
    "Invalid hyperlink - Object does not exist.": "Invalid hyperlink - Object does not exist.",
    "Invalid page.": "Invalid page.",
    "Invalid pk \"{pk_value}\" - object does not exist.": "Invalid pk \"{pk_value}\" - object does not exist.",
    "Invalid token header. No credentials provided.": "Invalid token header. No credentials provided.",
    "Invalid token header. Token string should not contain invalid characters.": "Invalid token header. Token string should not contain invalid characters.",
    "Invalid token header. Token string should not contain spaces.": "Invalid token header. Token string should not contain spaces.",
    "Invalid token.": "Invalid token.",
    "Invalid username/password.": "Invalid username/password.",
    "Invalid value.": "Invalid value.",
    "Invalid version in \"Accept\" header.": "Invalid version in \"Accept\" header.",
    "Invalid version in URL path.": "Invalid version in URL path.",
    "Invalid version in URL path. Does not match any version namespace.": "Invalid version in URL path. Does not match any version namespace.",
    "Invalid version in hostname.": "Invalid version in hostname.",
    "Invalid version in query parameter.": "Invalid version in query parameter.",
    "Key": "Key",
    "Malformed request.": "Malformed request.",
    "Method \"{method}\" not allowed.": "Method \"{method}\" not allowed.",
    "More than {count} items...": "More than {count} items...",
    "Must include \"username\" and \"password\".": "Must include \"username\" and \"password\".",
    "No file was submitted.": "No file was submitted.",
    "No filename could be determined.": "No filename could be determined.",
    "No items to select.": "No items to select.",
    "None": "None",
    "Not found.": "Not found.",
    "Object with {slug_name}={value} does not exist.": "Object with {slug_name}={value} does not exist.",
    "Ordering": "Ordering",
    "Password": "Password",
    "Permission denied.": "Permission denied.",
    "Request was throttled.": "Request was throttled.",
    "Search": "Search",
    "String value too large.": "String value too large.",
    "Submit": "Submit",
    "The fields {field_names} must make a unique set.": "The fields {field_names} must make a unique set.",
    "The submitted data was not a file. Check the encoding type on the form.": "The submitted data was not a file. Check the encoding type on the form.",
    "The submitted file is empty.": "The submitted file is empty.",
    "This field is required.": "This field is required.",
    "This field may not be blank.": "This field may not be blank.",
    "This field may not be null.": "This field may not be null.",
    "This field must be unique for the \"{date_field}\" date.": "This field must be unique for the \"{date_field}\" date.",
    "This field must be unique for the \"{date_field}\" month.": "This field must be unique for the \"{date_field}\" month.",
    "This field must be unique for the \"{date_field}\" year.": "This field must be unique for the \"{date_field}\" year.",
    "This field must be unique.": "This field must be unique.",
    "This list may not be empty.": "This list may not be empty.",
    "This selection may not be empty.": "This selection may not be empty.",
    "This value does not match the required pattern.": "This value does not match the required pattern.",
    "Time has wrong format. Use one of these formats instead: {format}.": "Time has wrong format. Use one of these formats instead: {format}.",
    "Token": "Token",
    "Tokens": "Tokens",
    "Unable to log in with provided credentials.": "Unable to log in with provided credentials.",
    "Unsupported media type \"{media_type}\" in request.": "Unsupported media type \"{media_type}\" in request.",
    "Upload a valid image. The file you uploaded was either not an image or a corrupted image.": "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
    "User": "User",
    "User account is disabled.": "User account is disabled.",
    "User inactive or deleted.": "User inactive or deleted.",
    "Username": "Username",
    "Value must be valid JSON.": "Value must be valid JSON.",
    "You do not have permission to perform this action.": "You do not have permission to perform this action.",
    "ascending": "ascending",
    "descending": "descending"
  };
  for (var key in newcatalog) {
    django.catalog[key] = newcatalog[key];
  }


  if (!django.jsi18n_initialized) {
    django.gettext = function(msgid) {
      var value = django.catalog[msgid];
      if (typeof(value) == 'undefined') {
        return msgid;
      } else {
        return (typeof(value) == 'string') ? value : value[0];
      }
    };

    django.ngettext = function(singular, plural, count) {
      var value = django.catalog[singular];
      if (typeof(value) == 'undefined') {
        return (count == 1) ? singular : plural;
      } else {
        return value.constructor === Array ? value[django.pluralidx(count)] : value;
      }
    };

    django.gettext_noop = function(msgid) { return msgid; };

    django.pgettext = function(context, msgid) {
      var value = django.gettext(context + '\x04' + msgid);
      if (value.indexOf('\x04') != -1) {
        value = msgid;
      }
      return value;
    };

    django.npgettext = function(context, singular, plural, count) {
      var value = django.ngettext(context + '\x04' + singular, context + '\x04' + plural, count);
      if (value.indexOf('\x04') != -1) {
        value = django.ngettext(singular, plural, count);
      }
      return value;
    };

    django.interpolate = function(fmt, obj, named) {
      if (named) {
        return fmt.replace(/%\(\w+\)s/g, function(match){return String(obj[match.slice(2,-2)])});
      } else {
        return fmt.replace(/%s/g, function(match){return String(obj.shift())});
      }
    };


    /* formatting library */

    django.formats = {
    "DATETIME_FORMAT": "N j, Y, P",
    "DATETIME_INPUT_FORMATS": [
      "%Y-%m-%d %H:%M:%S",
      "%Y-%m-%d %H:%M:%S.%f",
      "%Y-%m-%d %H:%M",
      "%Y-%m-%d",
      "%m/%d/%Y %H:%M:%S",
      "%m/%d/%Y %H:%M:%S.%f",
      "%m/%d/%Y %H:%M",
      "%m/%d/%Y",
      "%m/%d/%y %H:%M:%S",
      "%m/%d/%y %H:%M:%S.%f",
      "%m/%d/%y %H:%M",
      "%m/%d/%y"
    ],
    "DATE_FORMAT": "N j, Y",
    "DATE_INPUT_FORMATS": [
      "%Y-%m-%d",
      "%m/%d/%Y",
      "%m/%d/%y"
    ],
    "DECIMAL_SEPARATOR": ".",
    "FIRST_DAY_OF_WEEK": 0,
    "MONTH_DAY_FORMAT": "F j",
    "NUMBER_GROUPING": 3,
    "SHORT_DATETIME_FORMAT": "m/d/Y P",
    "SHORT_DATE_FORMAT": "m/d/Y",
    "THOUSAND_SEPARATOR": ",",
    "TIME_FORMAT": "P",
    "TIME_INPUT_FORMATS": [
      "%H:%M:%S",
      "%H:%M:%S.%f",
      "%H:%M"
    ],
    "YEAR_MONTH_FORMAT": "F Y"
  };

    django.get_format = function(format_type) {
      var value = django.formats[format_type];
      if (typeof(value) == 'undefined') {
        return format_type;
      } else {
        return value;
      }
    };

    /* add to global namespace */
    globals.pluralidx = django.pluralidx;
    globals.gettext = django.gettext;
    globals.ngettext = django.ngettext;
    globals.gettext_noop = django.gettext_noop;
    globals.pgettext = django.pgettext;
    globals.npgettext = django.npgettext;
    globals.interpolate = django.interpolate;
    globals.get_format = django.get_format;

    django.jsi18n_initialized = true;
  }

}(this));
