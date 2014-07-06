# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding field 'Field.to_field'
        db.add_column(u'app_field', 'to_field',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Field'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Field.to_field'
        db.delete_column(u'app_field', 'to_field_id')


    models = {
        u'app.field': {
            'Meta': {'object_name': 'Field'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edited': (
            'django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'null': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'regex': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'size_max': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'table': ('django.db.models.fields.related.ForeignKey', [],
                      {'related_name': "'app_field_table'", 'to': u"orm['app.Table']"}),
            'to_field': ('django.db.models.fields.related.ForeignKey', [],
                         {'to': u"orm['app.Field']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.IntegerField', [], {'max_length': '2'})
        },
        u'app.foreignkey': {
            'Meta': {'object_name': 'ForeignKey'},
            'destiny': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'app_foreign_key_destiny'", 'to': u"orm['app.Field']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [],
                       {'related_name': "'app_foreign_key_origin'", 'to': u"orm['app.Field']"})
        },
        u'app.project': {
            'Meta': {'object_name': 'Project'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edited': (
            'django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'app.table': {
            'Meta': {'object_name': 'Table'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'edited': (
            'django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [],
                        {'related_name': "'app_table_project'", 'to': u"orm['app.Project']"})
        }
    }

    complete_apps = ['app']