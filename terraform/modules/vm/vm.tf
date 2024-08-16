resource "azurerm_network_interface" "test" {
  name                = "${var.application_type}-${var.resource_type}-nw"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${var.public_ip}"
  }
}

resource "azurerm_linux_virtual_machine" "test" {
  name                = "${var.application_type}-${var.resource_type}-vm"
  location            = "${var.location}"
  resource_group_name = "${var.resource_group}"
  size                = "Standard_DS2_v2"
  admin_username      = "${var.admin_username}"
  admin_password      = "${var.admin_password}"
  disable_password_authentication = false
  network_interface_ids = [azurerm_network_interface.test.id]
  admin_ssh_key {
    username   = "${var.admin_username}"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCaifkK9g3Bd5bTWqWYj/EtGVmv67ZOKu9q4SnV5t50WFr3CS5yZx3+5Jlyq/70cFixaH7q2uVR7iqB54m+NslN83fI50mXqej8UEsi1ppmW7KG22NSxbKxFbR933vDS7Fo0+r9WPeNFrl4q59vHHV9UJ08e3AFKdaWsQef/ceM/kV4HzuYLQutVoouXYVA/2DaHZiqnSsadxZXu3VNvLQhfkytw5xhpWZEygyefOtJcve7oq0d6+BQ9nQPNqfaIsAQ9a9QoQni0C9jLRp8AyyeH9Q4tqMXzHbugnXYKNtr9Vu2nJsAOXzd3KQPg+7ScHHarVT1JckN8KYYOwkTPrVP4hCxfohLZ43S7gI2ea4nfqeg4EIM4Vh6FkpJmHwrdQ6jj8S+YsnWJdnhFmoeQNaG695MnRZipNhLTjWN9rhCtHD5Rlvh+xTbyfgLxwp8ByDgGz/jZghSPx4emRelu/APFUMPOU3paKcgZyf6dq2R8tJjcRl43pqq/Cn946j42kM= tieutuan@tieutuan"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
