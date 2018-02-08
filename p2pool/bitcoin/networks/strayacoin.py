import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'd0e1f5ec'.decode('hex')
P2P_PORT = 9666
ADDRESS_VERSION = 63
RPC_PORT = 9432
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'strayacoinprivkey' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getblockchaininfo())['chain'] != 'test'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 2.5 * 60 # s
SYMBOL = 'NAH'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'strayacoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/strayacoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.strayacoin'), 'strayacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://straya.network/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://straya.network/address/'
TX_EXPLORER_URL_PREFIX = 'http://straya.network/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**8
DUST_THRESHOLD = 0.03e8
