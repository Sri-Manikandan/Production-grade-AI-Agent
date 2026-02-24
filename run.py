import random
import asyncio
import inngest
from dotenv import load_dotenv

load_dotenv()

topics = [
    "Openclaw Usecases",
    "Openclaw Integration with Salesforce",
]

async def send_request(client, i):
    topic = random.choice(topics)
    
    event = inngest.Event(
        name="newsletter/generate", data={"topic":topic, "max_articles":3}
    )

    try:
        result = await client.send(event)
        print(f"{i}: {topic} -> SUCCESS")
    except Exception as e:
        print(f"{i}: {topic} -> FAILED: {str(e)}")


async def main():
    client = inngest.Inngest(
        app_id="newsletter_client",
        is_production=False,
    )

    tasks = [send_request(client,i) for i in range(1,4)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())