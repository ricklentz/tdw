# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class OverlapSphere(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsOverlapSphere(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = OverlapSphere()
        x.Init(buf, n + offset)
        return x

    # OverlapSphere
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # OverlapSphere
    def Id(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # OverlapSphere
    def ObjectIds(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(tdw.flatbuffers.number_types.Int32Flags, a + tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # OverlapSphere
    def ObjectIdsAsNumpy(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(tdw.flatbuffers.number_types.Int32Flags, o)
        return 0

    # OverlapSphere
    def ObjectIdsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # OverlapSphere
    def Env(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(tdw.flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def OverlapSphereStart(builder): builder.StartObject(3)
def OverlapSphereAddId(builder, id): builder.PrependInt32Slot(0, id, 0)
def OverlapSphereAddObjectIds(builder, objectIds): builder.PrependUOffsetTRelativeSlot(1, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(objectIds), 0)
def OverlapSphereStartObjectIdsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def OverlapSphereAddEnv(builder, env): builder.PrependBoolSlot(2, env, 0)
def OverlapSphereEnd(builder): return builder.EndObject()
