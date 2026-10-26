import struct


# ============================================================
# Protocol Settings
# ============================================================

MAGIC = 0x4652414D       # ASCII: "FRAM"

VERSION = 1

TYPE_FRAME = 0x01


# ============================================================
# Pixel Format
# ============================================================

# 灰階：每個像素 1 byte
PIXEL_FORMAT_GRAY8 = 0x01

# 彩色 BGR：每個像素 3 bytes
PIXEL_FORMAT_BGR24 = 0x02


# ============================================================
# Packet Structure
# ============================================================

HEADER_FORMAT = "<IBBIHHBI"

# Header:
#
# <    = Little Endian
# I    = uint32   MAGIC
# B    = uint8    VERSION
# B    = uint8    TYPE
# I    = uint32   FRAME_ID
# H    = uint16   WIDTH
# H    = uint16   HEIGHT
# B    = uint8    PIXEL_FORMAT
# I    = uint32   PAYLOAD_SIZE

HEADER_SIZE = struct.calcsize(HEADER_FORMAT)

CRC_SIZE = 4


# ============================================================
# TCP Settings
# ============================================================

# 對方電腦使用 TCP Port 5000
TCP_PORT = 5000


# ============================================================
# Network Settings
# ============================================================

# 我的電腦
LOCAL_IP = "192.168.1.2"

# 對方電腦
REMOTE_IP = "192.168.1.4"


# ============================================================
# Video Settings
# ============================================================

# 每秒取幾幀
SAMPLE_FPS = 10


# ============================================================
# Frame Settings
# ============================================================

MAX_FRAME_ID = 0xFFFFFFFF

MAX_WIDTH = 0xFFFF

MAX_HEIGHT = 0xFFFF

MAX_PAYLOAD_SIZE = 0xFFFFFFFF