import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def test_post_via_sendgrid():
    message = Mail(
        from_email='wgiersche@gmail.com',
        to_emails='wgiersche@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')

    try:
        apikey = os.environ.get('SENDGRID_API_KEY')
        sg = SendGridAPIClient(apikey)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


if __name__ == '__main__':
    test_post_via_sendgrid()
