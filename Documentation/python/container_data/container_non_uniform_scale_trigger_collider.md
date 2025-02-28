# ContainerNonUniformScaleTriggerCollider

`from tdw.container_data.container_non_uniform_scale_trigger_collider import ContainerNonUniformScaleTriggerCollider`

Data for a container trigger collider that can have a non-uniform scale.

***

## Fields

- `scale` The scale of the collider.

- `tag` The collider's semantic [`ContainerColliderTag`](container_collider_tag.md).

- `position` The collider's local position.

- `shape` The [`TriggerColliderShape`](../collision_data/trigger_collider_shape.md).

- `bottom_center_position` The bottom-center position of the collider. Unlike TDW objects, the true pivot of a trigger collider is at its centroid.

***

## Functions

#### \_\_init\_\_

**`ContainerNonUniformScaleTriggerCollider(tag, position, scale)`**

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| tag |  ContainerColliderTag |  | The collider's semantic [`ContainerColliderTag`](container_collider_tag.md). |
| position |  Dict[str, float] |  | The local position of the collider. |
| scale |  Dict[str, float] |  | The scale of the collider. |