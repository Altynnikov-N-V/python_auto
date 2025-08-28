import allure
from allure_commons.types import AttachmentType

def add_screenshot(browser):
    try:
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name="Screenshot",
            attachment_type=AttachmentType.PNG
        )
    except Exception:
        pass

def add_html(browser):
    try:
        allure.attach(
            browser.driver.page_source,
            name='page_source',
            attachment_type=AttachmentType.HTML,
        )
    except Exception:
        pass

def add_logs(browser):
    try:
        logs = '\n'.join([f"[{l['level']}] {l['message']}" for l in browser.driver.get_log('browser')])
        allure.attach(logs, name='browser_console', attachment_type=AttachmentType.TEXT)
    except Exception:
        pass

def add_video(browser):
    # для selenoid.autotests.cloud стандартная ссылка на видео по session_id
    try:
        session = browser.driver.session_id
        host = 'selenoid.autotests.cloud'
        url = f'https://{host}/video/{session}.mp4'
        allure.attach(url, name='video_url', attachment_type=AttachmentType.URI_LIST)
    except Exception:
        pass