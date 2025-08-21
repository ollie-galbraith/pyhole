import fnmatch

class Config():
    def __init__(self, parent):
        self.parent = parent
        self.base_parent = parent
        self.endpoint = '/config'
        
    def DNS(self):
        return self.DNSClass(self)

    class DNSClass():
        def __init__(self, parent):
            self.parent = parent
            self.base_parent = parent.base_parent
            self.endpoint = self.parent.endpoint + '/dns'

        def get(self):
            response = self.base_parent.get(self.endpoint)
            return response['config']['dns']
        
        def Hosts(self):
            return self.HostsClass(self)
        
        def CNames(self):
            return self.CNameClass(self)
        
        class HostsClass():
            def __init__(self, parent):
                self.parent = parent
                self.base_parent = parent.base_parent
                self.endpoint = self.parent.endpoint + "/hosts"
                
            def get(self, ip_address=None, domain=None):
                response = self.base_parent.get(self.endpoint)['config']['dns']['hosts']
                
                if ip_address is not None:
                    response = [record for record in response if fnmatch.fnmatch(record.split(' ')[0], ip_address)]
                if domain is not None:
                    response = [record for record in response if fnmatch.fnmatch(record.split(' ')[1], domain)]
                if len(response) == 0:
                    return None
                return response
            
            def create(self, ip_address, domain):
                endpoint = self.endpoint + f'/{ip_address} {domain}'
                self.base_parent.put(endpoint)

            def delete(self, ip_address, domain):
                endpoint = self.endpoint + f'/{ip_address} {domain}'
                self.base_parent.delete(endpoint)

            def update(self, ip_address, domain):
                endpoint = self.endpoint + f'/{ip_address} {domain}'
                self.base_parent.put(endpoint)
                
            def modify(self, ip_address, domain):
                endpoint = self.endpoint + f'/{ip_address} {domain}'
                self.base_parent.patch(endpoint)

        class CNameClass():
            def __init__(self, parent):
                self.parent = parent
                self.base_parent = parent.base_parent
                self.endpoint = self.parent.endpoint + "/cnameRecords"
                
            def get(self):
                response = self.base_parent.get(self.endpoint)
                return response['config']['dns']['cnameRecords']
            
            def create(self, domain, target):
                endpoint = self.endpoint + f'/{domain},{target}'
                self.base_parent.put(endpoint)
            
            def delete(self, domain, target):
                endpoint = self.endpoint + f'/{domain},{target}'
                self.base_parent.delete(endpoint)

