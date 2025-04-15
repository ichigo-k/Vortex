from config.gen_ai_config import model


def prompt(message):
    response = model.generate_content(message)
    return response.text
