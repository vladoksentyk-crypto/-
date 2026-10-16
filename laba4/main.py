from zovnishni.biblioteka_seaborn import run_seaborn_demo
from zovnishni.biblioteka_requests import run_requests_demo
from zovnishni.biblioteka_numpy import run_numpy_demo
from zovnishni.biblioteka_pandas import run_pandas_demo
from zovnishni.biblioteka_colorama import run_colorama_demo
from zovnishni.biblioteka_pyfiglet import run_pyfiglet_demo
from zovnishni.biblioteka_qrcode import run_qrcode_demo
from zovnishni.biblioteka_pillow import run_pillow_demo
from zovnishni.biblioteka_emoji import run_emoji_demo
from zovnishni.biblioteka_tabulate import run_tabulate_demo

from vbudovani.biblioteka_os import run_os_demo
from vbudovani.biblioteka_json import run_json_demo
from vbudovani.biblioteka_math import run_math_demo
from vbudovani.biblioteka_random import run_random_demo
from vbudovani.biblioteka_datetime import run_datetime_demo


def main():
    demos = [
        run_seaborn_demo, run_requests_demo, run_numpy_demo, run_pandas_demo,
        run_colorama_demo, run_pyfiglet_demo, run_qrcode_demo, run_pillow_demo,
        run_emoji_demo, run_tabulate_demo,
        run_os_demo, run_json_demo, run_math_demo, run_random_demo, run_datetime_demo,
    ]
    for demo in demos:
        print(demo())


if __name__ == "__main__":
    main()
