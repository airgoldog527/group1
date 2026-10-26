import struct
import zlib


# =========================
# Packet 基本設定
# =========================

MAGIC = 0x4652414D       # "FRAM"
VERSION = 1
TYPE_FRAME = 0x01

# Pixel Format
PIXEL_FORMAT_GRAY8 = 0x01
PIXEL_FORMAT_BGR24 = 0x02


HEADER_FORMAT = "<IBBIHHBI"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
CRC_SIZE = 4


# =========================
# 建立 Frame Packet
# =========================

def create_frame_packet(
    frame_id,
    width,
    height,
    payload,
    pixel_format=PIXEL_FORMAT_GRAY8
):

    payload_size = len(payload)

    header = struct.pack(
        HEADER_FORMAT,
        MAGIC,
        VERSION,
        TYPE_FRAME,
        frame_id,
        width,
        height,
        pixel_format,
        payload_size
    )

    crc = zlib.crc32(payload)

    crc_bytes = struct.pack(
        "<I",
        crc
    )

    return header + payload + crc_bytes


# =========================
# 解析 Frame Packet
# =========================

def parse_frame_packet(packet):

    if len(packet) < HEADER_SIZE + CRC_SIZE:
        raise ValueError("Packet 太短")

    header_data = packet[:HEADER_SIZE]

    (
        magic,
        version,
        packet_type,
        frame_id,
        width,
        height,
        pixel_format,
        payload_size
    ) = struct.unpack(
        HEADER_FORMAT,
        header_data
    )

    if magic != MAGIC:
        raise ValueError("MAGIC 錯誤")

    if version != VERSION:
        raise ValueError("VERSION 不支援")

    if packet_type != TYPE_FRAME:
        raise ValueError("Packet TYPE 錯誤")

    payload_start = HEADER_SIZE
    payload_end = payload_start + payload_size

    if len(packet) < payload_end + CRC_SIZE:
        raise ValueError("Packet 不完整")

    payload = packet[
        payload_start:payload_end
    ]

    received_crc = struct.unpack(
        "<I",
        packet[payload_end:payload_end + CRC_SIZE]
    )[0]

    calculated_crc = zlib.crc32(payload)

    if received_crc != calculated_crc:
        raise ValueError("CRC 檢查失敗")

    return {
        "frame_id": frame_id,
        "width": width,
        "height": height,
        "pixel_format": pixel_format,
        "payload_size": payload_size,
        "payload": payload,
    }