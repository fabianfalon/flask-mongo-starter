from src import create_app, APIException

app = create_app()


@app.errorhandler(APIException)
def generic_api_error_handler(exception):
    json_message = {"messages": [exception.to_dict()]}
    return json_message, exception.status_code


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
