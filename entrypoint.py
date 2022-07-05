import dotenv
from src.lambda_function import create_wc

dotenv.load_dotenv()
if __name__ == "__main__":
    create_wc(event=None, context=None)