from django.test import TestCase, tag

from testapp.models import Device

class DeviceModelTests(TestCase):

    @tag("devices-models")
    def test_can_save_device(self):
        dev_1 = Device(name="Dev1", key="ADSADSDAC")
        dev_1.save()
        self.assertEqual(Device.objects.count(), 1)