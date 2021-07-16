import os
from datetime import datetime


def create_list(dirname, subdir, subdir2, subdir3):
    html = "<tr>" + \
           "  <td>" + dirname + "</td>" + \
           "  <td>" + subdir + "</td>" + \
           "  <td>" + subdir2 + "</td>" + \
           "  <td>" + subdir3 + "</td>" + \
           "</tr>"
    return html


def read_images_from_path(source_path):
    dirname = ""
    subdir = ""
    subdir2 = ""
    subdir3 = ""
    html = ""
    if os.path.isdir(os.path.join(source_path)):
        print("test")
    else:
        html = html + create_list(source_path)

    for dirname in os.listdir(source_path):
        if os.path.isdir(os.path.join(os.path.join(source_path, dirname))):
            for subdir in os.listdir(os.path.join(source_path, dirname)):
                if os.path.isdir(os.path.join(source_path, dirname, subdir)):
                    for subdir2 in os.path.join(source_path, dirname, subdir):
                        if os.path.isdir(os.path.join(source_path, dirname, subdir, subdir2)):
                            for subdir3 in os.listdir(os.path.join(source_path, dirname, subdir, subdir2)):
                                html = html + create_list(dirname, subdir, subdir2, subdir3)
                        else:
                            html = html + create_list(dirname, subdir, subdir2, subdir3)
                else:
                    html = html + create_list(dirname, subdir, subdir2, subdir3)
        else:
            html = html + create_list(dirname, subdir, subdir2, subdir3)
    return html


def generate_html(source_path, target_path):
    """
    HTML code has been adapted from:
    https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_filters_table&stacked=h

    :param source_path:
    :param target_path:
    :return:
    """
    title = "Image File Index " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    html_code = ""
    html_code = html_code + \
                "<!doctype html>\n" + \
                "<html lang=\"en\">\n" + \
                "<head>\n" + \
                "<meta charset=\"utf-8\">\n" + \
                "<title>" + title + "</title>\n" + \
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">" + \
                "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css\">" + \
                "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js\"></script>" + \
                "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js\"></script>" + \
                "</head>\n" + \
                "<body>\n" + \
                "<div class=\"container\">\n" + \
                "<h2 class=\"display-1\">" + title + "</h2>\n" + \
                "<p>Type something in the input field to search the table for first names, last names or emails:</p>" + \
                "<input class=\"form-control\" id=\"myInput\" type=\"text\" placeholder=\"Search..\">" + \
                "<br />" + \
                "<table class=\"table table-bordered table-striped\">" + \
                "<thead>" + \
                "  <tr>" + \
                "    <th>Top Folder</th>" + \
                "    <th>Material</th>" + \
                "    <th>Setting</th>" + \
                "    <th>File</th>" + \
                "  </tr>" + \
                "</thead>" + \
                "<tbody id=\"myTable\">"
    """
    Loop through Folders and Create index details
    """
    html_code = html_code + read_images_from_path(source_path)
    html_code = html_code + "</div>\n</body>"
    """
    Do not forget the query script
    """
    html_code = html_code + \
                "<script>" + \
                "$(document).ready(function(){" + \
                "    $(\"#myInput\").on(\"keyup\", function() {" + \
                "        var value = $(this).val().toLowerCase();" + \
                "        $(\"#myTable tr\").filter(function() {" + \
                "            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)" + \
                "        });" + \
                "    });" + \
                "});" + \
                "</script>" + \
                "</html>"
    f = open(os.path.join(target_path, "image_index.html"), "w")
    f.write(html_code)
    f.close()


def create_index(read_from, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path, mode=777)
    # Creates HTML file image_index.html
    generate_html(read_from, output_path)
