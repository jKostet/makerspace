from application import app

# heroku logs
import os
if os.environ.get("HEROKU"):
	app.logger.addHandler(logging.StreamHandler(sys.stdout))
	app.logger.setLevel(logging.ERROR)

# TODO: Remember to remove debug mode later
if __name__ == '__main__':
	app.run(debug=True)
