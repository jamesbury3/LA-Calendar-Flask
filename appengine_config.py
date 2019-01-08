import dev_appserver
dev_appserver.fix_sys_path()
from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
vendor.add('lib')