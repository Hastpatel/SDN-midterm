try:
    import netmiko
    from netmiko import ConnectHandler
    import regex as re
    import time
    import json
    from datetime import datetime
    from flask import Flask, Response, render_template
    from mininet_ip import *
    from mininet_topology import *
    from ssh_router import *
except:
    print("install required modules")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart-data')
def chart_data():
    def packet_data():
        p=0
        while True:
            pingall()
            p=flows()
            print(p)
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': p})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(packet_data(), mimetype='text/event-stream')


if __name__=='__main__':
    print('start')
    ip=ip_leased()
    print('Ip leased to mininet VM: {}'.format(ip))
    mininet_init()
    controller_config()
    time.sleep(5)
    print('mininet topology done')
    router1()
    time.sleep(60)
    print('R1 config done')
    router2()
    time.sleep(60)
    print('R2 config done')
    router3()
    time.sleep(60)
    print('R3 config done')
    print('mininet controller set')
    controller_connectivity()
    print('see mininet controller')
    app.run(threaded=True)
