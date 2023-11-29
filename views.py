def my_view(request):
    user_name = request.get("user").get("Name")


    status_code = 200

    message = f"Hello {user_name}! I'm glad to greeting you!"

    return {
        "status_code": status_code,
        "respons": message
    }