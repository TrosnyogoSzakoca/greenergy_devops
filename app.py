from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def swap_case():
    try:
        input_string = request.form.get('string')
        if not input_string:
            raise ValueError("Missing 'string' parameter in the request.")
        if input_string.isdigit():
            raise ValueError("Invalid input type. Expecting a string.")

        swapped_string = input_string.swapcase()
        return jsonify({'result': swapped_string})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()
