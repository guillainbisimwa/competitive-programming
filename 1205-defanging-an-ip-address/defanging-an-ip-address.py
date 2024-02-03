class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_ip = address.replace('.', '[.]')
        return defanged_ip
        