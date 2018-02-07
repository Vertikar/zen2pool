from p2pool.bitcoin import networks

PARENT = networks.nets['strayacoin']
SHARE_PERIOD = 0.5 * 60 # seconds
CHAIN_LENGTH = 3*60*60//15 # shares
REAL_CHAIN_LENGTH = 3*60*60//15 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'e30d71731ae64889'.decode('hex')
PREFIX = 'b2021af67edf5411'.decode('hex')
P2P_PORT = 8444
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9444
BOOTSTRAP_ADDRS = 'mxblue.net.au p2pool.nahyeah.network p2pool.straya.network'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True