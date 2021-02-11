#replace username,password and URL
#       connect('Username','password','t3://URL:7001')
# to run script you will need to to source env.
#       $source /opt/vbms/weblogic/wlserver/server/bin/setWLSEnv.sh
# run command
#       $java weblogic.WLST get_serverstate.py

from java.io import FileInputStream
import java.lang
import os
import string

connect('bdavid','<r6xjL5_Tx:?56Tw','t3://vbms000.perf.vbms.vba.va.gov:7001')

allServers=domainRuntimeService.getServerRuntimes();

if (len(allServers) > 0):

  for tempServer in allServers:

    jdbcServiceRT = tempServer.getJDBCServiceRuntime();

    dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();

    if (len(dataSources) > 0):

        for dataSource in dataSources:

	    print 'Name                               '  ,  dataSource.getName()
	    print 'Properties                         '  ,  dataSource.getProperties()
	    print 'DeploymentState                    '  ,  dataSource.getDeploymentState()
	    print 'Parent                             '  ,  dataSource.getParent()
            print 'Properties                         '  ,  dataSource.getProperties()
            print 'ReserveRequestCount                '  ,  dataSource.getReserveRequestCount()
            print 'State                              '  ,  dataSource.getState()
            print 'Type                               '  ,  dataSource.getType()
            print 'VersionJDBCDriver                  '  ,  dataSource.getVersionJDBCDriver()
            print 'ActiveConnectionsAverageCount      '  ,  dataSource.getActiveConnectionsAverageCount()
            print 'ActiveConnectionsCurrentCount      '  ,  dataSource.getActiveConnectionsCurrentCount()
            print 'ActiveConnectionsHighCount         '  ,  dataSource.getActiveConnectionsHighCount()
            print 'ConnectionDelayTime                '  ,  dataSource.getConnectionDelayTime()
            print 'ConnectionsTotalCount              '  ,  dataSource.getConnectionsTotalCount()
            print 'CurrCapacity                       '  ,  dataSource.getCurrCapacity()
            print 'CurrCapacityHighCount              '  ,  dataSource.getCurrCapacityHighCount()
            print 'FailedReserveRequestCount          '  ,  dataSource.getFailedReserveRequestCount()
            print 'FailuresToReconnectCount           '  ,  dataSource.getFailuresToReconnectCount()
            print 'HighestNumAvailable                '  ,  dataSource.getHighestNumAvailable()
            print 'HighestNumUnavailable              '  ,  dataSource.getHighestNumUnavailable()
            print 'LeakedConnectionCount              '  ,  dataSource.getLeakedConnectionCount()
            print 'ModuleId                           '  ,  dataSource.getModuleId()
            print 'NumAvailable                       '  ,  dataSource.getNumAvailable()
            print 'NumUnavailable                     '  ,  dataSource.getNumUnavailable()
            print 'ReserveRequestCount                '  ,  dataSource.getReserveRequestCount()
	    print "------------------------------------------------------------------------"

