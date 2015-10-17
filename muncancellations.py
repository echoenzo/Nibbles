"""
muncancellations.py - MUN Cancellation Module
Author: Enzo

Returns current cancellations of MUN classes from http://www.mun.ca/main/cancellations.php
"""

from sopel import web
from sopel.module import commands
from sopel.formatting import bold
from lxml import html
from dateutil import parser
from datetime import datetime

uri = 'http://www.mun.ca/main/cancellations.php'

@commands('canceldetail')
def cancelled(bot, trigger):
    """Show current cancelled classes at MUN"""
    page, headers = web.get(uri, return_headers=True)
    if headers['_http_status'] != 200:
        bot.say('Couldn\'t find cancellation information.')
        return
    parsed = html.fromstring(page)
    middle = parsed.get_element_by_id('middle')
    contents = list(middle)
    reply = []
    if trigger.nick != trigger.sender:
        bot.reply('I\'m messaging you with a detailed cancellation list!')
    for element in contents:
        if element.tag=='p' and element.text_content() == '________________________________________':
            break
        elif element.tag=='h2':
            printed = True
            text = element.text_content()
            day = parser.parse(text)
            if day.date() == datetime.today().date():
                reply.append('MUN\'s Cancellations for ' + bold(text) + ' (TODAY):')
            else:
                reply.append('MUN\'s Cancellations for ' + bold(text) + ': ')
        elif element.tag=='p':
            text = element.text_content()
            course = list(element)[0].text_content()
            reply.append(bold(course) + text[len(course):])
    for a in reply:
        bot.msg(trigger.nick, a)
    

@commands('cancellations')
def short_cancelled(bot, trigger):
    """Display short list of cancelled courses at MUN"""
    page, headers = web.get(uri, return_headers=True)
    if headers['_http_status'] != 200:
        bot.say('Couldn\'t find cancellation information.')
        return
    parsed = html.fromstring(page)
    middle = parsed.get_element_by_id('middle')
    contents = list(middle)
    reply = ''
    for element in contents:
        if element.tag=='p' and element.text_content() == '________________________________________':
            break
        elif element.tag=='h2':
            printed = True
            text = element.text_content()
            day = parser.parse(text)
            if day.date() == datetime.today().date():
                reply += '| MUN\'s Cancellations for ' + bold(text) + ' (TODAY): '
            else:
                reply += '| MUN\'s Cancellations for ' + bold(text) + ': '
        elif element.tag=='p':
            text = element.text_content()
            course = list(element)[0].text_content()
            reply += course + ', '
    bot.say(reply[2:-2])
    bot.say('Use \'.canceldetail\' for more detailed information')
