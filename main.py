from custom_logger.logger import CustomLogger

if __name__ == '__main__':

    # logger = CustomLogger()
    logger = CustomLogger.from_config_json("config.json")

    logger.debug("debugging")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")
