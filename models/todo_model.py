from odoo import models, fields
class TodoTask(models.Model):
	_name = 'todo.task'
	_description = 'Tareas Pendientes'
	name = fields.Char('Descripcion', required=True)
	is_done = fields.Boolean('Hecho?')
	active = fields.Boolean('Activo?', default=True)