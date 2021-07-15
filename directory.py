import os

downloadPaths = [
    "../vanguardia-api/assets",

    "../vanguardia-api/assets/avatar_1x",
    "../vanguardia-api/assets/avatar_2x",
    "../vanguardia-api/assets/avatar_thumb_1x",
    "../vanguardia-api/assets/avatar_thumb_2x",

    "../vanguardia-api/assets/list_medium_1x",
    "../vanguardia-api/assets/list_medium_2x",
    "../vanguardia-api/assets/list_large_1x",

    "../vanguardia-api/assets/paragraph_image_large_desktop_1x",
    "../vanguardia-api/assets/paragraph_image_large_desktop_2x",
    "../vanguardia-api/assets/paragraph_image_desktop_1x",
    "../vanguardia-api/assets/paragraph_image_desktop_2x",
    "../vanguardia-api/assets/paragraph_image_table_1x",
    "../vanguardia-api/assets/paragraph_image_table_2x",
    "../vanguardia-api/assets/paragraph_image_phone_1x",
    "../vanguardia-api/assets/paragraph_image_phone_2x"
    ]

def createDirectory():
    create = lambda path: os.mkdir(path)
    for path in downloadPaths:
        try:
            create(path)
        except OSError:
            print ("Creation of the directory %s failed" % path)
        else:
            print ("Successfully created the directory %s " % path)

# createDirectory()