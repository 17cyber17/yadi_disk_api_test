from selenium.webdriver.common.by import By

class BasePageLocators():
    RECENT_LINK = (By.CSS_SELECTOR, '[href="/client/recent"]')
    DISK_LINK = (By.CSS_SELECTOR, '#/disk')
    PHOTO_LINK = (By.CSS_SELECTOR, '[href="/client/photo"]')
    ALBUMS_LINK = (By.CSS_SELECTOR, '[href="/client/albums"]')
    SHARED_LINK = (By.CSS_SELECTOR, '[href="/client/shared"]')
    JOURNAL_LINK = (By.CSS_SELECTOR, '[href="/client/journal"]')
    ATTACH_LINK = (By.CSS_SELECTOR, '[href="/client/attach"]')
    TRASH_LINK = (By.CSS_SELECTOR, '[href="/client/trash"]')