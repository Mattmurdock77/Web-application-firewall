# Flask Web Application Firewall (WAF)

This is a simple web application firewall (WAF) built with Flask and Python regular expressions to block malicious input such as SQL injection, XSS, and other common attacks.

## Setup

1. Clone the repository:

    ```bash
    git clone <repo_url>
    cd waf_project
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python app.py
    ```

4. Test the application by making requests. If a malicious pattern is detected, the server will respond with a `400 Bad Request` status.

## Configurations

- The WAF rules are stored in `config.py`. You can modify the `patterns` list to include additional regular expressions to block more types of malicious input.

## License

This project is open source and available under the MIT License.
