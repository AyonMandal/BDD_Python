import pdb
from _datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Helpers.Logger import CreateLogger


def before_all(context):
    context.browser = context.config.userdata['browser']
    # print(context.browser)


def before_feature(context, feature):
    # setting up logger

    feature_name = "_".join(feature.name.split(" "))
    current_time = datetime.now().strftime('_%Y%m%d_%H%M%S')
    filename = feature_name + current_time
    context.start_logger = CreateLogger.logger_creation("Logs\\{}".format(filename))

    # determining which browser to use

    try:

        if context.browser == 'Firefox':
            context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif context.browser == 'Chrome':
            context.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif context.browser == 'Edge':
            context.driver = webdriver.Edge(EdgeChromiumDriverManager(log_level='INFO').install())
        else:
            context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.start_logger.info("{} browser started successfully!".format(context.browser.upper()))

    except Exception as e:
        context.start_logger.error(e)
        raise


def before_scenario(context, scenario):
    # initiate logging of scenario

    scenario_name = "_".join(scenario.name.split(" --")[0].split(" "))
    context.start_logger.info("{}".format("*" * 60))
    context.start_logger.info("{}".format(scenario_name.upper()))
    context.start_logger.info("{}".format("*" * 60))


def after_scenario(context, scenario):
    scenario_name = "_".join(scenario.name.split(" --")[0].split(" "))
    context.start_logger.info("End of scenario : {}".format(scenario_name))
    context.start_logger.info("--------------------- Closing Logs, Bye Bye :-) -------------------------")


def after_feature(context, feature):
    context.driver.quit()
