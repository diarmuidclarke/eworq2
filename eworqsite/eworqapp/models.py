from django.db import models


class eWORQ_Request(models.Model):
    eWORQ_ID = models.BigIntegerField('eWORQ ID')
    eWORQ_raised_date = models.DateTimeField('date raised')
    eWORQ_requestor_userID = models.CharField(max_length=20)
    eWORQ_project = models.CharField(max_length=50)
    eWORQ_project_desc = models.CharField(max_length=2000)
    eWORQ_copyfiles_src_dir = models.CharField(max_length=2000)
    eWORQ_copyfiles_dest_dir = models.CharField(max_length=2000)
    eWORQ_manualwork_desc = models.CharField(max_length=20000)
    eWORQ_request_status = models.CharField(max_length=30)

    def __str__(self):
        return 'ID:' + self.eWORQ_ID.__str__()


class eWORQ_CopyFile(models.Model):
    eworq_id_f = models.ForeignKey(eWORQ_Request, on_delete=models.CASCADE)
    filename = models.CharField(max_length=2000)
    
    def __str__(self):
        return 'FILE:' + self.filename


class eWORQ_Rejection(models.Model):
    eworq_id_f = models.ForeignKey(eWORQ_Request, on_delete=models.CASCADE)
    reason = models.CharField(max_length=2000)
    rejector_userID = models.CharField(max_length=20)
    rejection_date = models.DateTimeField('date rejected')
    
    def __str__(self):
        return 'REJ:' + self.reason


class eWORQ_Approval(models.Model):
    eworq_id_f = models.ForeignKey(eWORQ_Request, on_delete=models.CASCADE)
    approver_userID = models.CharField(max_length=20)
    approval_date = models.DateTimeField('date approved')

    def __str__(self):
        return 'APPROVAL of ID:' + self.approver_userID


class ElevatedUsers(models.Model):
    elev_userID = models.CharField(max_length=20)
    elev_user_is_executor = models.BooleanField(default=False)
    elev_user_is_approver = models.BooleanField(default=False)
    elev_user_is_EQA_approver = models.BooleanField(default=False)

    def __str__(self):
        return 'Elevated ID:' + self.elev_userID
