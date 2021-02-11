#replace username,password and URL
#       connect('Username','password','t3://URL:7001')
# to run script you will need to to source env.
#       $source /opt/vbms/weblogic/wlserver/server/bin/setWLSEnv.sh
# run command
#       $java weblogic.WLST get_serverstate.py
# also replace username,password and URL

#connect([username],[password],[admin url])
connect('bdavid','<r6xjL5_Tx:?56Tw','t3://vbms000.perf.vbms.vba.va.gov:7001')
servers=cmo.getServers()
print "-------------------------------------------------------"
print "\t"+cmo.getName()+" domain status"
print "-------------------------------------------------------"
for server in servers:
        state(server.getName(),server.getType())
print "-------------------------------------------------------"

cd ('AppDeployments')
myapps=cmo.getAppDeployments()
print "-------------------------------------------------------"

for appName in myapps:
       domainConfig()
       cd ('/AppDeployments/'+appName.getName()+'/Targets')
       mytargets = ls(returnMap='true')
       domainRuntime()
       cd('AppRuntimeStateRuntime')
       cd('AppRuntimeStateRuntime')
       for targetinst in mytargets:
             curstate4=cmo.getCurrentState(appName.getName(),targetinst)
             print '-----------', curstate4, '-----------', appName.getName()

