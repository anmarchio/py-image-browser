HTML_HEAD = "<!doctype html>\n" + \
            "<html lang=\"en\">\n" + \
            "<head>\n" + \
            "<meta charset=\"utf-8\">\n" + \
            "<title>Image File List</title>\n" + \
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" + \
            "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\">\n" + \
            "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js\"></script>\n" + \
            "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js\"></script>\n" + \
            "</head>\n"

BODY_HEAD = "<body>\n" + \
            "<div class=\"container\">\n" + \
            "<h2 class=\"display-1\">Image File List</h2>\n" + \
            "<p>Type something in the input field to search the table for file names:</p>\n" + \
            "<input class=\"form-control\" id=\"myInput\" type=\"text\" placeholder=\"Search..\">\n" + \
            "<br />\n" + \
            "<table class=\"table table-bordered table-striped\">\n" + \
            "<thead>\n" + \
            "  <tr>" + \
            "    <th>Folder</th>\n" + \
            "    <th>File</th>\n" + \
            "  </tr>\n" + \
            "</thead>\n" + \
            "<tbody id=\"myTable\">\n"
BODY_CLOSE_TAG = "</tbody></table></div>\n</body>"
QUERY_SCRIPT = "<script>\n" + \
               "$(document).ready(function(){\n" + \
               "    $(\"#myInput\").on(\"keyup\", function() {\n" + \
               "        var value = $(this).val().toLowerCase();\n" + \
               "        $(\"#myTable tr\").filter(function() {\n" + \
               "            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)\n" + \
               "        });\n" + \
               "    });\n" + \
               "});\n" + \
               "</script>\n" + \
               "</html>"

DEFAULT_FILE_NAME = "image_index.html"

IMAGE_FILE_FORMATS = ['.bmp', '.gif', '.jpg', '.jpeg', '.png', '.tif', '.tiff']