AM_CXXFLAGS = @CXXFLAGS@ \
	@MYSQLCLIENT_CFLAGS@ \
	@LIBXML2_CFLAGS@ \
	-I../../metrutil/include \
	-L../../metrutil/lib \
	-g -O0 -Wall
AM_CFLAGS = @CFLAGS@ \
	@MYSQLCLIENT_CFLAGS@ \
	@LIBXML2_CFLAGS@ \
	-I../../metrutil/include \
	-L../../metrutil/lib \
	-g -O0 -Wall



bin_PROGRAMS = \
	project_api \

project_api_SOURCES = \
	
project_api_LDADD = \
	-lmetrutil \
	-lcurl \
	-lxml2 \
	-lcrypt \
	@LIBMICROHTTPD_LIBS@ \
	@LIBCCEXT2_LIBS@ \
	@MYSQLCLIENT_LIBS@
project_api_LDFLAGS = \
	-static \
	@MYSQLCLIENT_LDFLAGS@
