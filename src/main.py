#!/usr/bin/env python3

import time, argparse, threading, logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())
from singleton import Singleton
from strand import Strand
from tickr import Tickr
from tickr_mock import TickrMock

def main():
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    parser.add_argument('-m', '--mac', help='clear the display on exit')
    args = parser.parse_args()

    logging.info(f'MAC is {args.mac}')
    logging.info('Press Ctrl-C to quit.')

    if not args.clear:
        logging.info('Use "-c" argument to clear LEDs on exit')

    tickr = Tickr.instance()
    tickr.connect(args.mac)
    tickr.subscribe()
    strand = Strand.instance()

    try:
        while True:
            strand.do_stuff(tickr.get_heart_rate())
            time.sleep(1)

    except KeyboardInterrupt:
        logging.info("Exiting...")
        tickr.disconnect() # also stops delegate thread
        logging.info("Disconnected")
        if args.clear:
            logging.info("Do light clear stuff here")
        os.sys.exit(0)

if __name__ == "__main__":
    main()