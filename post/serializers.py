from rest_framework import serializers

from .models import (
    JobPostStatus,
    SkillSet,
    JobPostSkillSet,
    JobType,
    JobPost,
    Company,
    CompanyBusinessArea,
    BusinessArea,
    JobPostActivity
)


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ("id", "job_type")


class CompanySerializer(serializers.ModelSerializer):


    class Meta:
        model = Company
        fields = ("id", "company_name")


class JobPostSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    skiilsets = serializers.SerializerMethodField()
    position_type = serializers.SerializerMethodField()
    def get_skiilsets(self, obj):
        print("obj=", end=""), print(obj.jobpostskillset_set.all())
        return [i.skill_set.name for i in obj.jobpostskillset_set.all()]

    # job_type = JobTypeSerializer()
    def get_position_type(self, obj):
        # print("obj=", end=""), print(obj.jobpostskillset_set.all())
        return obj.job_type.job_type

    class Meta:
        model = JobPost
        fields = ('id', 'position_type', 'company', 'job_description', 'salary', 'skiilsets')

        extra_kwargs = {
            'job_type': {
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                },
                # required : validator에서 해당 값의 필요 여부를 판단한다.
                'required': False  # default : True
            },
        }

# job_post = JobPostSerializer(read_only=True)


class JobPostSkillSetSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    job_post = JobPostSerializer(read_only=True)


    # jobs = serializers.SerializerMethodField()
    # jobs_list = serializers.ListSerializer()
    #
    # def get_jobs(self,obj):
    #     # company_list = []
    #     print("obj =",end=""), print(obj.job_post.id)
    #     if obj.job_post.id not in self.jobs_list:
    #         self.jobs_list.append(obj.job_post.id)
    #     return company_list

    class Meta:
        model = JobPostSkillSet
        fields = ('id', 'skill_set', 'job_post')

class JobPostActivitySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        job_post_activity = JobPostActivity.objects.create(
            **validated_data
        )
        job_post_status = JobPostStatus.objects.filter(status = 'submitted').get()
        job_post_activity.job_post_status = job_post_status
        job_post_activity.save()
        return job_post_activity
    class Meta:
        model = JobPostActivity
        fields = '__all__'
