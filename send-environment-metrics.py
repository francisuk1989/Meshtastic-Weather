from meshtastic import portnums_pb2, telemetry_pb2

# For connection over serial
# import meshtastic.serial_interface
# interface = meshtastic.serial_interface.SerialInterface()

# For connection over TCP
import meshtastic.tcp_interface
interface = meshtastic.tcp_interface.TCPInterface(hostname='192.168.2.89', noProto=False)

# NODE ID to send the weather infomation
BROADCAST_ADDR = XXXXXX

# Grab the Weather info
file1 = open('AirQuality')
sendAirQuality = file1.readlines()
file2 = open('Humidity')
sendHumidity = file2.readlines()
file3 = open('Pressure')
sendPressure = file3.readlines()
file4 = open('Temperature')
sendTemperature = file4.readlines()

# Send data to the node
telemetry_data = telemetry_pb2.Telemetry()

for line in sendTemperature:
    print("telemetry_data.environment_metrics.temperature = {}".format(line.strip()))

for line in sendHumidity:
    print("telemetry_data.environment_metrics.relative_humidity = {}".format(line.strip()))

for line in sendPressure:
    print("telemetry_data.environment_metrics.barometric_pressure = {}".format(line.strip()))

for line in sendAirQuality:
    print("telemetry_data.environment_metrics.gas_resistance = {}".format(line.strip()))
    
interface.sendData(
    telemetry_data,
    destinationId=BROADCAST_ADDR,
    portNum=portnums_pb2.PortNum.TELEMETRY_APP,
    wantResponse=False,
)

interface.close()
