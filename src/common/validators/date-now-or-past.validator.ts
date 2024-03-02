import {
  ValidatorConstraint,
  ValidatorConstraintInterface,
} from 'class-validator';

@ValidatorConstraint({ name: 'dateNowOrPastValidator', async: false })
export class DateNowOrPastValidator implements ValidatorConstraintInterface {
  validate(created_at: Date) {
    const now = new Date();
    const createdAt = new Date(created_at);
    return createdAt.getTime() <= now.getTime();
  }

  defaultMessage() {
    return 'It is not possible to use a future date';
  }
}
