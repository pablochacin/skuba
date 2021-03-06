/*
 * Copyright (c) 2019 SUSE LLC.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

package cluster

import (
	"github.com/SUSE/skuba/pkg/skuba"
)

type ScaffoldFile struct {
	Location    string
	Content     string
	DoNotRender bool
}

var (
	criScaffoldFiles = map[string][]ScaffoldFile{
		"sysconfig": {
			{
				Location: skuba.CriDockerDefaultsConfFile(),
				Content:  criDockerDefaultsConf,
			},
		},
		"criconfig": {
			{
				Location: skuba.CriDefaultsConfFile(),
				Content:  criDefaultsConf,
			},
			{
				Location: skuba.CriConfFolderReadmeFile(),
				Content:  CriConfFolderReadme,
			},
		},
	}

	cloudScaffoldFiles = map[string][]ScaffoldFile{
		"openstack": {
			{
				Location: skuba.CloudReadmeFile(),
				Content:  cloudReadme,
			},
			{
				Location: skuba.OpenstackCloudConfTemplateFile(),
				Content:  openstackCloudConfTemplate,
			},
			{
				Location: skuba.OpenstackReadmeFile(),
				Content:  openstackReadme,
			},
		},
		"aws": {
			{
				Location: skuba.CloudReadmeFile(),
				Content:  cloudReadme,
			},
			{
				Location: skuba.AWSReadmeFile(),
				Content:  awsReadme,
			},
		},
		"vsphere": {
			{
				Location: skuba.CloudReadmeFile(),
				Content:  cloudReadme,
			},
			{
				Location: skuba.VSphereCloudConfTemplateFile(),
				Content:  vSphereCloudConfTemplate,
			},
			{
				Location: skuba.VSphereReadmeFile(),
				Content:  vSphereReadme,
			},
		},
		"azure": {
			{
				Location: skuba.CloudReadmeFile(),
				Content:  cloudReadme,
			},
			{
				Location: skuba.AzureCloudConfTemplateFile(),
				Content:  azureCloudConfTemplate,
			},
			{
				Location: skuba.AzureReadmeFile(),
				Content:  azureReadme,
			},
		},
	}
)
