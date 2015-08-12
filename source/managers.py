# -*- coding: utf-8 -*-
"""
    Based off ecs: https://github.com/seanfisk/ecs
@author: Kotarou
"""

from color import *

class EntityManager(object):
    """
        Manage all entities in the game.
        For speed of access, three dicts are used to store the entities/components in the game
    """
    def __init__(self):

        # [type][owning entity][entity id] -> component
        self._dbComponent = {}
        # [owning entity][component id] -> component
        self._dbEntity = {}
        # [component id] -> component
        self._dbCID = {}

    @property
    def componentDatabase(self):
        """ Direct modification of the database is not allowed """
        return self._dbComponent

    @property
    def entityDatabase(self):
        """ Direct modification of the database is not allowed """
        return self._dbEntity

    @property
    def cidDatabase(self):
        """ Direct modification of the database is not allowed """
        return self._dbCID

    def addComponent(self, entity, component):
        """
            When a component is added to an entity, add that component to our database
        """
        component.owner = entity

        cType = type(component)
        print(cType, component.cid)
        if cType not in self._dbComponent:
            self._dbComponent[cType] = {entity: {}}

        if entity not in self._dbComponent[cType]:
            self._dbComponent[cType][entity] = {}

        self._dbComponent[cType][entity][component.cid] = component

        if entity not in self._dbEntity:
            self._dbEntity[entity] = {}

        self._dbEntity[entity][component.cid] = component

        self._dbCID[component.cid] = component



    def removeComponentByID(self, entity, cid):
        """
            Remove component from entity by cid
        """
        try:
            cType = type(self._dbEntity[entity][cid])
            del self._dbEntity[entity][cid]
            del self._dbComponent[cType][entity][cid]
            del self._dbCID[cid]
            # TODO remove emtpy fields
        except KeyError:
            pass

    def removeComponentsByType(self, entity, cType):
        """
            Removes all components of type cType from entity
        """
        try:
            remove = [(j,k) for j,k in self._dbEntity[entity].items() if type(k) == cType]
            for (j,k) in remove:
                del self._dbEntity[entity][j]
                del self._dbCID[j.cid]

            del self._dbComponent[cType][entity]
            if self._dbComponent[cType] == {}:
                del self._dbComponent[cType]

        except KeyError:
            pass

    def getComponentByID(self, cid):
        """
            Get a component using its ID
        """
        try:
            return self._dbCID[cid]
        except KeyError:
            return None

    def pairsForType(self, cType):
        """
        	Returns a list of (entity, [component]) tuples, where each component is of cType
        """
        try:
            #x = [(j,k.values()) for (j,k) in self._dbComponent[cType].items()]
            return [(k.owner, k) for (j,k) in self._dbCID.items() if type(k) == cType]
        except KeyError:
        	return None

    def componentsForEntity(self, entity):
        """
            Return all components belonging to entity
        """
        return self._dbEntity[entity].items()

    def componentByType(self,entity, cType):
        """
            Return all components of type cType belongning to entity
        """
        try:
            return [k for (j,k) in self._dbCID.items() if type(k) == cType and k.owner == entity]
        except KeyError:
            return None

class SystemManager(object):
    """
        Manages all the interior systems.
    """

    def __init__(self, eman):
        self._dbSystems = {}
        self.eman = eman

    @property
    def systems(self):
        return self._dbSystems

    def addSystem(self, manager, system):
        sType = type(system)

        if manager not in self._dbSystems:
            self._dbSystems[manager] = [] # {}

        # TODO: Logic for duplicate systems
        system.eman = self.eman
        system.sman = self

        self._dbSystems[manager].append(system)

    def update(self, manager, dt):
        """
            Update each system under manager in the order they were added
        """
        for system in self._dbSystems[manager]:
            system.update(dt)



# class Component:
#     def __init__(self, cid):
#         self.cid = cid

#     def __hash__(self):
#         return self.cid

# class Component2:
#     def __init__(self, cid):
#         self.cid = cid

#     def __hash__(self):
#         return self.cid

# class Entity:
#     def __init__(self, cid):
#         self.cid = cid

#     def __hash__(self):
#         return self.cid

if __name__ == "__main__":
    pass
    # a = EntityManager()
    # x = Entity(0)
    # y = Entity(1)

    # b = Component(0)
    # c = Component(1)
    # d = Component2(3)
    # e = Component2(4)

    # a.addComponent(x, b)
    # a.addComponent(x, c)
    # print(a.componentsForEntity(x))
    # a.removeComponentByID(x, 0)
    # print(a.componentsForEntity(x))
    # a.addComponent(x, d)
    # print(a.componentsForEntity(x))
    # a.removeComponentsByType(x, type(b))
    # print(a.componentsForEntity(x))

    # a.addComponent(y,d)
    # a.addComponent(y,e)
    # print(a.pairsForType(type(c)))

        # We do not need to keep track of the next color ID, as that is provided by Color.next()
        # All components have a component id (cid)
        # Some components will have a seperate colorID (handle) for mouse interactions / etc
