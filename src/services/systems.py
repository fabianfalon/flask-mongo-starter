""""
System Service
"""
import logging

from mongoengine import ValidationError

from src.services.services import Service
from src.models.system_manager import SystemManager
from src.exceptions import ResourceNotFound

logger = logging.getLogger("services")


class SystemServices(Service):
    entity = SystemManager

    def create(self, data: dict) -> SystemManager:

        sku = data.get("SKU") if data.get("SKU") else data.get("sku")
        emei = data.get("EMEI") if data.get("EMEI") else data.get("emei")

        system = self.entity(
            installerId=data.get("installerId", ""),
            installerName=data.get("installerName", ""),
            enclosureSerialNumber=data.get("enclosureSerialNumber", ""),
            workingState=data.get("workingState", ""),
            simSerialNumber=data.get("simSerialNumber", ""),
            pendingSystemStatus=data.get("pendingSystemStatus", ""),
            systemId=data.get("systemId", ""),
            companyId=data.get("companyId", ""),
            companyName=data.get("companyName", ""),
            vendor=data.get("vendor", ""),
            sku=sku,
            emei=emei,
            devices=data.get("devices", []),
            location=data.get("location", {}),
            solarStrings=data.get("solarStrings", []),
            systemConfig=data.get("systemConfig", {}),
            setupState=data.get("setupState", ""),
            setupStatus=data.get("setupStatus", "")
        )
        entity = system.save()
        logger.info("System created successfully")
        return entity

    def get_system_by_id(self, entity_id: str) -> SystemManager:
        entity = self._get_system(entity_id)
        return entity

    @staticmethod
    def _get_system(entity_id: str) -> SystemManager:
        try:
            entity = SystemManager.objects.with_id(entity_id)
        except ValidationError:
            # search with emei
            try:
                entity = SystemManager.objects(emei=str(entity_id)).get()
            except Exception:
                entity = SystemManager.objects(enclosureSerialNumber=str(entity_id)).get()
            except Exception:
                entity = None
        if not entity:
            raise ResourceNotFound(
                message="Entity with this parameter: {id} not found".format(
                    id=entity_id
                )
            )
        return entity

    @staticmethod
    def _clean_system_payload(data: dict) -> dict:
        sku = data.pop("SKU") if data.get("SKU") else data.pop("sku")
        emei = data.pop("EMEI") if data.get("EMEI") else data.pop("emei")

        data["emei"] = emei
        data["sku"] = sku

        if "createdAt" in data:
            data.pop("createdAt")
        if "id" in data:
            data.pop("id")
        return data

    def update(self, entity_id: str, data: dict) -> SystemManager:
        data = self._clean_system_payload(data)
        self.entity.objects(id=str(entity_id)).update(**data)
        entity = self.get_by_id(entity_id)
        return entity


system_srv = SystemServices()
