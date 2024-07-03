from selenium.webdriver.common.by import By
import configparser


class PropertiesUtils:
    def __init__(self, properties_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(properties_file_path)

    def get_locator(self, web_element_name):
        locator_type_and_value = self.config.get("Locators", web_element_name)
        locator_type, locator_value = locator_type_and_value.split("~")

        # Convert the locator type to uppercase for consistency
        locator_type = locator_type.upper()

        # Mapping between locator types and By class constants
        locator_mapping = {
            "ID": By.ID,
            "NAME": By.NAME,
            "TAGNAME": By.TAG_NAME,
            "LINKTEXT": By.LINK_TEXT,
            "PARTIALLINKTEXT": By.PARTIAL_LINK_TEXT,
            "XPATH": By.XPATH,
            "CSSSELECTOR": By.CSS_SELECTOR,
            "CLASSNAME": By.CLASS_NAME,
        }

        # Handling unknown locator types
        if locator_type in locator_mapping:
            return locator_mapping[locator_type], locator_value
        else:
            # Raise an exception for unknown locator types
            raise ValueError(f"Unknown locator type: {locator_type}")
