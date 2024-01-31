from flask import Flask, render_template, request, make_response

app = Flask(__name__)

# Sample data storage (replace with a database in a real-world application)
gpa_data = []

@app.route('/calculate', methods=['GET', 'POST'])
def gpa_calculator():
    if request.method == 'POST':
        subject = request.form['subject']
        credits = float(request.form['credits'])
        grade = float(request.form['grade'])
        weighted_points = credits * grade

        # Store the data
        gpa_data.append({
            'subject': subject,
            'credits': credits,
            'grade': grade,
            'weighted_points': weighted_points
        })
        # Create a response with a 200 OK status code
        response = make_response(render_template('index.html', gpa_data=gpa_data))
        response.status_code = 200
        return response

    # Render the HTML template with data from the server
    return render_template('index.html', gpa_data=gpa_data)


@app.route('/results', methods=['GET'])
def final_gpa():
    # Calculate the sum of 'weighted_points' in gpa_data
    total_weighted_points = sum(entry['weighted_points'] for entry in gpa_data)
    return render_template('results.html', gpa_data = gpa_data, total_weighted_points=total_weighted_points)



if __name__ == '__main__':
    app.run(debug=True)
