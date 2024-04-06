# import libraries
import os
import links
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

# load in dotenv data
load_dotenv()

cat_url = links.get_random_cat()

# grab data from dotenv and assign to variables
slack_token = os.environ.get("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

# print text and cat image link to channel
try:
    response = client.chat_postMessage(
        channel=os.environ.get("SLACK_CHANNEL_ID"),
        blocks=[
            {
                "type": "section",
                "text": {
                        "type": "mrkdwn",
                        "text": "*Here is the daily cat!*"
                    },
            },
            {
                "image_url": f"{cat_url}",
                "type": "image",
                "alt_text": "Daily cat image"
            }
        ]
    )
except SlackApiError as e:
    # raise error if needed
    raise e