from _datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Helpers.Logger import CreateLogger


def before_feature(context, feature):
    print("I am executed before all")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


def before_scenario(context, scenario):
    scenario_name = "_".join(scenario.name.split(" --")[0].split(" "))
    current_time = datetime.now().strftime('_%Y%m%d_%H%M%S')
    filename = scenario_name + current_time
    context.start_logger = CreateLogger.logger_creation("Logs\\{}".format(filename))

    context.start_logger.info("Logger ready for logging scenario : {}".format(scenario_name))


def after_scenario(context, scenario):
    scenario_name = "_".join(scenario.name.split(" --")[0].split(" "))
    context.start_logger.info("End of scenario : {}".format(scenario_name))
    context.start_logger.info("--------------------- Closing Logs, Bye Bye :-) -------------------------")


def after_feature(context, feature):
    context.driver.quit()
