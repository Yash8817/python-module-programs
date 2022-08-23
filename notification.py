from player import notification
title = "hello people"
messgae = "thank you for reading"


notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)