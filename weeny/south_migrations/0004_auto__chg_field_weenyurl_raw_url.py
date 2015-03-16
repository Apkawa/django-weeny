# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WeenyURL.raw_url'
        db.alter_column(u'weeny_weenyurl', 'raw_url', self.gf('django.db.models.fields.URLField')(max_length=4096, null=True))

    def backwards(self, orm):

        # Changing field 'WeenyURL.raw_url'
        db.alter_column(u'weeny_weenyurl', 'raw_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'weeny.urltracking': {
            'Meta': {'ordering': "[u'weeny_url', u'weeny_site__site', u'timestamp', u'user_agent']", 'object_name': 'URLTracking'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'target_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeny.WeenyURL']"}),
            'user_agent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeny.UserAgent']"}),
            'weeny_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeny.WeenySite']"}),
            'weeny_url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'weeny.useragent': {
            'Meta': {'ordering': "[u'browser_family', u'os_family', u'browser_version', u'os_version']", 'object_name': 'UserAgent'},
            'browser_family': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'browser_version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'device_family': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_bot': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_pc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_tablet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_touch_capable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'os_family': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'os_version': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ua_string': ('django.db.models.fields.TextField', [], {})
        },
        u'weeny.weenysite': {
            'Meta': {'unique_together': "([u'site', u'short_domain'],)", 'object_name': 'WeenySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'default': "u'https'", 'max_length': '10'}),
            'redirect_short_domain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'requires_moderation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seed': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '62', 'blank': 'True'}),
            'short_domain': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'track': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'weeny.weenyurl': {
            'Meta': {'ordering': "[u'weeny_site']", 'unique_together': "([u'weeny_site', u'urlcode'],)", 'object_name': 'WeenyURL'},
            'allow_revisit': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'contenttype_set_for_weenyurl'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_removed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_visited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'raw_url': ('django.db.models.fields.URLField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'track': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'urlcode': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '10', 'blank': 'True'}),
            'weeny_site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['weeny.WeenySite']"})
        }
    }

    complete_apps = ['weeny']