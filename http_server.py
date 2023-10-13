import esphome.config_validation as cv
from esphome import automation
from esphome.const import CONF_ID, CONF_PORT, CONF_PATH, CONF_REQUEST, CONF_RESPONSE, CONF_TEXT_SENSOR
from esphome.core import App, Application

http_server_ns = cv.ns

HTTPServer = http_server_ns.class_(
    "HTTPServer", 
    cv.Component,
    cv.Schema({
        cv.GenerateID(CONF_ID): cv.declare_id(HTTPServer),
        cv.Required(CONF_PORT): cv.port,
        cv.Required(CONF_PATH): cv.string,
        cv.Required(CONF_REQUEST): cv.string,
        cv.Required(CONF_RESPONSE): cv.string,
    }),
)
