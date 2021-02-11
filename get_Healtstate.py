#replace username,password and URL
# 	connect('Username','password','t3://URL:7001')
# to run script you will need to to source env.
# 	$source /opt/vbms/weblogic/wlserver/server/bin/setWLSEnv.sh
# run command 
#	$java weblogic.WLST get_serverstate.py


from java.io import FileInputStream
import java.lang
import os
import string


connect('bdavid','<r6xjL5_Tx:?56Tw','t3://vbms000.perf.vbms.vba.va.gov:7001')

domainRuntime()

cd('ServerRuntimes')

servers=domainRuntimeService.getServerRuntimes()
for server in servers:
     serverName=server.getName();
     print '**************************************************'
     print '##############' , serverName,'###############'
     print '**************************************************'
     print '### Server State         ####', server.getState()
     print '### Server ListenAddress ####', server.getListenAddress()
     print '### Server ListenPort    ####', server.getListenPort()
     print '### Server Health State  ####', server.getHealthState()
