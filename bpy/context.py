import sys
import typing
import bpy

active_base: 'bpy.types.ObjectBase' = None

active_bone: 'bpy.types.EditBone' = None

active_gpencil_brush: 'bpy.types.GPencilSculptBrush' = None

active_gpencil_frame: list = None

active_gpencil_layer: typing.List['bpy.types.GPencilLayer'] = None

active_gpencil_palette: typing.List['bpy.types.GPencilPalette'] = None

active_gpencil_palettecolor: typing.List[
    'bpy.types.GPencilPaletteColor'] = None

active_node: 'bpy.types.Node' = None

active_object: 'bpy.types.Object' = None

active_operator: 'bpy.types.Operator' = None

active_pose_bone: 'bpy.types.PoseBone' = None

area: 'bpy.types.Area' = None

armature: 'bpy.types.Armature' = None

blend_data: 'bpy.types.BlendData' = None

bone: 'bpy.types.Bone' = None

brush: 'bpy.types.Brush' = None

camera: 'bpy.types.Camera' = None

cloth: 'bpy.types.ClothModifier' = None

collision: 'bpy.types.CollisionModifier' = None

curve: 'bpy.types.Curve' = None

dynamic_paint: 'bpy.types.DynamicPaintModifier' = None

edit_bone: 'bpy.types.EditBone' = None

edit_image: 'bpy.types.Image' = None

edit_mask: 'bpy.types.Mask' = None

edit_movieclip: 'bpy.types.MovieClip' = None

edit_object: 'bpy.types.Object' = None

edit_text: 'bpy.types.Text' = None

editable_bases: typing.List['bpy.types.ObjectBase'] = None

editable_bones: typing.List['bpy.types.EditBone'] = None

editable_gpencil_layers: typing.List['bpy.types.GPencilLayer'] = None

editable_gpencil_strokes: typing.List['bpy.types.GPencilStroke'] = None

editable_objects: typing.List['bpy.types.Object'] = None

fluid: 'bpy.types.FluidSimulationModifier' = None

gpencil_data = None

gpencil_data_owner: 'bpy.types.ID' = None

image_paint_object: 'bpy.types.Object' = None

lamp: 'bpy.types.Lamp' = None

lattice: 'bpy.types.Lattice' = None

line_style: 'bpy.types.FreestyleLineStyle' = None

material: 'bpy.types.Material' = None

material_slot: 'bpy.types.MaterialSlot' = None

mesh: 'bpy.types.Mesh' = None

meta_ball: 'bpy.types.MetaBall' = None

mode: typing.Union[int, str] = None

object: 'bpy.types.Object' = None

particle_edit_object: 'bpy.types.Object' = None

particle_settings: 'bpy.types.ParticleSettings' = None

particle_system: 'bpy.types.ParticleSystem' = None

particle_system_editable: 'bpy.types.ParticleSystem' = None

pose_bone: 'bpy.types.PoseBone' = None

region: 'bpy.types.Region' = None

region_data: 'bpy.types.RegionView3D' = None

scene: 'bpy.types.Scene' = None

screen: 'bpy.types.Screen' = None

sculpt_object: 'bpy.types.Object' = None

selectable_bases: typing.List['bpy.types.ObjectBase'] = None

selectable_objects: typing.List['bpy.types.Object'] = None

selected_bases: typing.List['bpy.types.ObjectBase'] = None

selected_bones: typing.List['bpy.types.EditBone'] = None

selected_editable_bases: typing.List['bpy.types.ObjectBase'] = None

selected_editable_bones: typing.List['bpy.types.EditBone'] = None

selected_editable_objects: typing.List['bpy.types.Object'] = None

selected_editable_sequences: typing.List['bpy.types.Sequence'] = None

selected_nodes: typing.List['bpy.types.Node'] = None

selected_objects: typing.List['bpy.types.Object'] = None

selected_pose_bones: typing.List['bpy.types.PoseBone'] = None

selected_sequences: typing.List['bpy.types.Sequence'] = None

sequences: typing.List['bpy.types.Sequence'] = None

smoke: 'bpy.types.SmokeModifier' = None

soft_body: 'bpy.types.SoftBodyModifier' = None

space_data: 'bpy.types.Space' = None

speaker: 'bpy.types.Speaker' = None

texture: 'bpy.types.Texture' = None

texture_slot: 'bpy.types.MaterialTextureSlot' = None

texture_user: 'bpy.types.ID' = None

texture_user_property: 'bpy.types.Property' = None

tool_settings: 'bpy.types.ToolSettings' = None

user_preferences: 'bpy.types.UserPreferences' = None

vertex_paint_object: 'bpy.types.Object' = None

visible_bases: typing.List['bpy.types.ObjectBase'] = None

visible_bones: typing.List['bpy.types.EditBone'] = None

visible_gpencil_layers: typing.List['bpy.types.GPencilLayer'] = None

visible_objects: typing.List['bpy.types.Object'] = None

visible_pose_bones: typing.List['bpy.types.PoseBone'] = None

weight_paint_object: 'bpy.types.Object' = None

window: 'bpy.types.Window' = None

window_manager: 'bpy.types.WindowManager' = None

world: 'bpy.types.World' = None
